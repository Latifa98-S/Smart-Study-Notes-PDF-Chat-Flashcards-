import { useState } from "react";

export default function UploadPDF({ onTextExtracted }) {
  const [loading, setLoading] = useState(false);

  const uploadPDF = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    setLoading(true);

    const res = await fetch("http://127.0.0.1:8000/upload-pdf", {
      method: "POST",
      body: formData
    });

    const data = await res.json();
    onTextExtracted(data.text);
    setLoading(false);
  };

  return (
    <div className="bg-slate-900 p-4 rounded-xl shadow-md flex items-center justify-between">
      <label className="cursor-pointer text-blue-400 hover:text-blue-300">
        📎 Upload PDF
        <input
          type="file"
          accept="application/pdf"
          onChange={uploadPDF}
          className="hidden"
        />
      </label>

      {loading && <span className="text-slate-400">Extracting...</span>}
    </div>
  );
}