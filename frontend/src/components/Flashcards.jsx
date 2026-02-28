import { useState } from "react";

export default  function Flashcards() {

const [context, setContext ] = useState("")
const [flashcards, setFlashcards] = useState("");
  const [loading, setLoading] = useState(false);

  const generateFlashcards = async () => {
    if (!context.trim()) return;

    setLoading(true);
    setFlashcards("");

    try {
      const res = await fetch("http://localhost:8000/flashcards", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ context })
      });

      const data = await res.json();
      setFlashcards(data.flashcards);
    } catch (err) {
      setFlashcards("Error generating flashcards.");
    }

    setLoading(false);
  };

  return (
    <div style={{ maxWidth: 800, margin: "40px auto" }}>
      <h2> Flashcards Generator</h2>
        
      <textarea
        value={context}
        onChange={(e) => setContext(e.target.value)}
        placeholder="Paste your lecture notes or context here..."
        rows={8}
        style={{ width: "100%", padding: 10 }}
      />
        <button> <onabort> 
            </onabort></button>
      <button
        onClick={generateFlashcards}
        style={{ marginTop: 10, padding: "6px 12px" }}
      >
        Generate Flashcards
      </button>

      {loading && <p><em>Generating flashcards...</em></p>}

      {flashcards && (
        <div
          style={{
            marginTop: 20,
            padding: 12,
            border: "1px solid #ccc",
            background: "#fafafa",
            whiteSpace: "pre-wrap"
          }}
        >
          {flashcards}
        </div>
      )}
    </div>
  );
}