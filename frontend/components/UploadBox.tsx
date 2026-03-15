"use client";

import { useState } from "react";
import { uploadDocument } from "../lib/api";

export default function UploadBox() {
  const [file, setFile] = useState<File | null>(null);
  const [docId, setDocId] = useState("");

  const handleUpload = async () => {
    if (!file) return;

    const data = await uploadDocument(file);
    setDocId(data.document_id);
  };

  return (
    <div className="p-6 border rounded-lg">
      <h2 className="text-xl font-bold mb-3">Upload IPO Prospectus</h2>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files?.[0] || null)}
      />

      <button
        onClick={handleUpload}
        className="bg-blue-600 text-white px-4 py-2 mt-3 rounded"
      >
        Upload
      </button>

      {docId && (
        <p className="mt-3 text-green-600">
          Document ID: {docId}
        </p>
      )}
    </div>
  );
}
