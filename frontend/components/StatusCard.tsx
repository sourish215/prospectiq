"use client";

import { useEffect, useState } from "react";
import { getStatus } from "../lib/api";

export default function StatusCard({ docId }: { docId: string }) {
  const [status, setStatus] = useState("");

  useEffect(() => {
    const interval = setInterval(async () => {
      const data = await getStatus(docId);
      if (data.length) {
        setStatus(data[0].status);
      }
    }, 3000);

    return () => clearInterval(interval);
  }, [docId]);

  return (
    <div className="border p-4 mt-4">
      <h3 className="font-semibold">Processing Status</h3>
      <p>{status}</p>
    </div>
  );
}
