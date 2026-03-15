"use client";

import { useState } from "react";
import { askQuestion } from "../lib/api";

export default function ChatWindow() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const handleAsk = async () => {
    const res = await askQuestion(question);
    setAnswer(JSON.stringify(res.results));
  };

  return (
    <div className="border p-6 mt-6">
      <h2 className="text-xl font-bold mb-3">Ask About the IPO</h2>

      <input
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        className="border p-2 w-full"
        placeholder="Ask about risks, revenue, etc..."
      />

      <button
        onClick={handleAsk}
        className="bg-green-600 text-white px-4 py-2 mt-3 rounded"
      >
        Ask
      </button>

      {answer && (
        <div className="mt-4">
          <h3 className="font-semibold">Answer</h3>
          <p>{answer}</p>
        </div>
      )}
    </div>
  );
}
