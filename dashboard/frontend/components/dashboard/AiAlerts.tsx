export default function AiAlerts() {

  const alerts = [
    "High congestion detected in Chennai route",
    "Storm risk increasing near Delhi hub",
    "AI predicts shipment delays in Zone 4",
    "Flight OPS latency rising by 12%",
  ];

  return (

    <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6">

      <h2 className="text-2xl font-bold mb-6">
        AI Operational Alerts
      </h2>

      <div className="space-y-4">

        {alerts.map((alert, index) => (

          <div
            key={index}
            className="
              bg-red-500/10
              border
              border-red-500/20
              text-red-400
              p-4
              rounded-xl
            "
          >
            {alert}
          </div>

        ))}

      </div>

    </div>

  );

}