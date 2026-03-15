import UploadBox from "../components/UploadBox";
import ChatWindow from "../components/ChatWindow";

export default function Home() {
  return (
    <main className="max-w-3xl mx-auto mt-10">

      <h1 className="text-3xl font-bold mb-6">
        ProspectIQ
      </h1>

      <UploadBox />

      <ChatWindow />

    </main>
  );
}
