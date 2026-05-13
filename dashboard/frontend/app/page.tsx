"use client";

import Sidebar from "@/components/dashboard/sidebar";
import KpiCard from "@/components/dashboard/KpiCard";
import AiAlerts from "@/components/dashboard/AiAlerts";
import AnalyticsChart from "@/components/dashboard/AnalyticsChart";

import { useEffect, useState } from "react";
import axios from "axios";

export default function Home() {

  const [backendStatus, setBackendStatus] =
    useState("Connecting...");

  const [shipments, setShipments] =
    useState<any[]>([]);

  // ✅ IMPORTANT: use Cloud Shell backend URL (NOT localhost)
  const API_URL =
    "/api/backend";

  // ---------------- BACKEND STATUS ----------------
  useEffect(() => {

    axios
      .get(`${API_URL}/`)
      .then((response) => {

        setBackendStatus(response.data.status);

      })
      .catch((error) => {

        console.error("Backend Error:", error);

        setBackendStatus("Backend Offline");

      });

  }, []);

  // ---------------- LIVE SHIPMENT STREAM ----------------
  useEffect(() => {

    const fetchShipments = async () => {

      try {

        const response =
          await axios.get(`${API_URL}/stream`);

        setShipments(
          response.data.live_feed.reverse()
        );

      } catch (error) {

        console.error(
          "Shipment Stream Error:",
          error
        );

      }

    };

    fetchShipments();

    const interval =
      setInterval(fetchShipments, 5000);

    return () => clearInterval(interval);

  }, []);

  return (

    <main className="flex bg-black text-white min-h-screen">

      <Sidebar />

      <div className="flex-1 p-10 overflow-auto">

        <div className="mb-10">

          <h1 className="text-5xl font-bold">
            Logistics Command Center
          </h1>

          <p className="mt-4 text-gray-400 text-xl">
            Enterprise AI Operations Dashboard
          </p>

        </div>

        {/* KPI CARDS */}
        <div className="grid grid-cols-3 gap-6">

          <KpiCard
            title="Backend Status"
            value={backendStatus}
            color="text-green-400"
          />

          <KpiCard
            title="Active Shipments"
            value={String(shipments.length)}
            color="text-blue-400"
          />

          <KpiCard
            title="AI Predictions"
            value="98%"
            color="text-purple-400"
          />

        </div>

        {/* AI ALERTS */}
        <div className="mt-10">
          <AiAlerts />
        </div>

        {/* ANALYTICS */}
        <div className="mt-10">
          <AnalyticsChart />
        </div>

        {/* SHIPMENT TABLE */}
        <div className="mt-10 bg-zinc-900 rounded-2xl border border-zinc-800 p-6">

          <h2 className="text-3xl font-bold mb-6">
            Live Shipment Intelligence
          </h2>

          <div className="overflow-x-auto">

            <table className="w-full">

              <thead>

                <tr className="text-left border-b border-zinc-700 text-gray-400">

                  <th className="pb-4">Shipment</th>
                  <th className="pb-4">Weather</th>
                  <th className="pb-4">Traffic</th>
                  <th className="pb-4">Risk Score</th>
                  <th className="pb-4">Status</th>

                </tr>

              </thead>

              <tbody>

                {shipments.map((item, index) => (

                  <tr
                    key={index}
                    className="border-b border-zinc-800 hover:bg-zinc-800/40 transition-all"
                  >

                    <td className="py-4 font-semibold">
                      {item.shipment.shipment_id}
                    </td>

                    <td className="py-4 capitalize">
                      {item.shipment.weather}
                    </td>

                    <td className="py-4 capitalize">
                      {item.shipment.traffic}
                    </td>

                    <td className="py-4">
                      {item.analysis.risk_score}
                    </td>

                    <td className="py-4">
                      <span className="bg-red-500/20 text-red-400 px-3 py-1 rounded-lg text-sm">
                        {item.analysis.status}
                      </span>
                    </td>

                  </tr>

                ))}

              </tbody>

            </table>

          </div>

        </div>

      </div>

    </main>

  );
}