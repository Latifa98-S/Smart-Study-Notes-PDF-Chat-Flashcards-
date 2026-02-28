import { useState } from "react";
import Chat from "./components/Chat";
import UploadPDF from "./components/UploadPDF";

export default function App() {
  const [pdfText, setPdfText] = useState("");

  return (
    <div className="min-h-screen flex flex-col items-center p-6">
      
      {/* Header */}
      <div className="w-full max-w-4xl mb-6">
        <h1 className="text-3xl font-bold text-center">
          📘 Smart Study Notes
        </h1>
        <p className="text-center text-slate-400 mt-2">
          Upload your PDF and chat with your notes
        </p>
      </div>

      {/* PDF Upload */}
      <div className="w-full max-w-4xl mb-4">
        <UploadPDF onTextExtracted={setPdfText} />
      </div>

      {/* Chat */}
      <div className="w-full max-w-4xl flex-1">
        <Chat context={pdfText} />
      </div>
    </div>
  );
}