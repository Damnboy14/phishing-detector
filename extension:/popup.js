document.getElementById("check").addEventListener("click", async () => {
  const url = document.getElementById("url").value;

  if (!url) {
    document.getElementById("result").innerText = "Please enter a URL";
    return;
  }

  try {
    const response = await fetch("http://127.0.0.1:5000/check", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url })
    });

    const data = await response.json();
    document.getElementById("result").innerText = data.result;
    document.getElementById("result").style.color = data.result.includes("Phishing") ? "red" : "green";

  } catch (err) {
    document.getElementById("result").innerText = "Error connecting to API";
  }
});
