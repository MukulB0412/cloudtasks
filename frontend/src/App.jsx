import { useEffect, useState } from "react";

function App() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/tasks")
      .then((res) => res.json())
      .then((data) => setTasks(data));
  }, []);

  return (
    <div className="min-h-screen bg-gray-900 text-white p-10">
      <h1 className="text-4xl font-bold text-center text-blue-400 mb-10">
        🚀 DevTasks Dashboard
      </h1>
      <div className="max-w-2xl mx-auto space-y-4">
        {tasks.map((task) => (
          <div
            key={task.id}
            className="bg-gray-800 p-4 rounded-lg shadow-md border border-gray-700"
          >
            <h2 className="text-xl text-blue-200 font-semibold">{task.title}</h2>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
