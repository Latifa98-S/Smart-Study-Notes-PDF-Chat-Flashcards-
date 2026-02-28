export default function Message({ role, text }) {
  const isUser = role === "user";

  return (
    <div
      style={{
        display: "flex",
        justifyContent: isUser ? "flex-end" : "flex-start",
        marginBottom: 8
      }}
    >
      <div
        style={{
          maxWidth: "75%",
          padding: "8px 12px",
          borderRadius: 8,
          background: isUser ? "#d1e7ff" : "#eaeaea"
        }}
      >
        <strong>{isUser ? "You" : "AI"}:</strong> {text}
      </div>
    </div>
  );
}