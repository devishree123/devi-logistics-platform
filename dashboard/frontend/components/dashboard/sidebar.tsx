export default function Sidebar() {
  return (
    <div className="w-64 h-screen bg-zinc-950 border-r border-zinc-800 p-6">

      <h1 className="text-3xl font-bold text-white">
        DEVI AI
      </h1>

      <p className="text-gray-500 mt-2">
        Logistics Control
      </p>

      <div className="mt-10 space-y-5">

        <div className="text-white bg-zinc-900 p-3 rounded-xl">
          Operations
        </div>

        <div className="text-gray-400 hover:text-white cursor-pointer">
          Shipments
        </div>

        <div className="text-gray-400 hover:text-white cursor-pointer">
          AI Intelligence
        </div>

        <div className="text-gray-400 hover:text-white cursor-pointer">
          Analytics
        </div>

        <div className="text-gray-400 hover:text-white cursor-pointer">
          Flight Ops
        </div>

        <div className="text-gray-400 hover:text-white cursor-pointer">
          Maps
        </div>

        <div className="text-gray-400 hover:text-white cursor-pointer">
          Monitoring
        </div>

      </div>
    </div>
  );
}