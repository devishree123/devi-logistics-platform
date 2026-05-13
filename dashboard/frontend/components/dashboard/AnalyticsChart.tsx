"use client";

import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
} from "recharts";

const data = [
  { day: "Mon", shipments: 120 },
  { day: "Tue", shipments: 210 },
  { day: "Wed", shipments: 180 },
  { day: "Thu", shipments: 260 },
  { day: "Fri", shipments: 320 },
  { day: "Sat", shipments: 280 },
  { day: "Sun", shipments: 350 },
];

export default function AnalyticsChart() {

  return (

    <div
      className="
        bg-zinc-900
        border
        border-zinc-800
        rounded-2xl
        p-6
        shadow-xl
      "
    >

      <h2 className="text-2xl font-bold mb-6">
        Shipment Analytics
      </h2>

      <div className="h-[350px]">

        <ResponsiveContainer width="100%" height="100%">

          <LineChart data={data}>

            <CartesianGrid strokeDasharray="3 3" />

            <XAxis dataKey="day" />

            <YAxis />

            <Tooltip />

            <Line
              type="monotone"
              dataKey="shipments"
              stroke="#3b82f6"
              strokeWidth={4}
            />

          </LineChart>

        </ResponsiveContainer>

      </div>

    </div>

  );

}