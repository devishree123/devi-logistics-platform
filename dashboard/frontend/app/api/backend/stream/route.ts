import { NextResponse } from "next/server";

const BACKEND_URL = "http://localhost:8000";

export async function GET() {
  try {
    const res = await fetch(`${BACKEND_URL}/stream`, {
      cache: "no-store",
    });

    const data = await res.json();

    return NextResponse.json(data);
  } catch (err) {
    return NextResponse.json(
      { live_feed: [] },
      { status: 500 }
    );
  }
}