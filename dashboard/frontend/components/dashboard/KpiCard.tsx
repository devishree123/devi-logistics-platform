type Props = {
  title: string;
  value: string;
  color: string;
};

export default function KpiCard({
  title,
  value,
  color,
}: Props) {

  return (

    <div
      className="
      bg-zinc-900
      border
      border-zinc-800
      rounded-2xl
      p-6
      shadow-xl
      hover:scale-105
      transition-all
      duration-300
    "
    >

      <h2 className="text-gray-400 text-lg">
        {title}
      </h2>

      <p
        className={`text-5xl font-bold mt-4 ${color}`}
      >
        {value}
      </p>

    </div>

  );

}