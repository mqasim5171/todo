document.addEventListener("DOMContentLoaded", function () {
  const taskList = document.getElementById("task-list");
  const addTaskButton = document.getElementById("add-task");
  const newTaskInput = document.getElementById("new-task");

  // Get CSRF token from cookies (default Django behavior)
  function getCSRFToken() {
    const name = "csrftoken=";
    const decodedCookie = decodeURIComponent(document.cookie);
    const ca = decodedCookie.split(';');
    for (let i = 0; i < ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return ""; // If CSRF token is not found
  }

  // Fetch the CSRF token from the cookies
  const csrfToken = getCSRFToken();

  // Fetch tasks from the Django API and display them
  function loadTasks() {
    fetch("http://127.0.0.1:8000/api/tasks/")
      .then(response => response.json())
      .then(tasks => {
        taskList.innerHTML = ""; // Clear existing tasks
        tasks.forEach(task => {
          const taskElement = document.createElement("div");
          taskElement.className = "task";
          if (task.completed) {
            taskElement.classList.add("completed");
          }
          taskElement.innerHTML = `
            <span>${task.title}</span>
            <button class="remove-task" data-id="${task.id}">Remove</button>
          `;
          taskList.appendChild(taskElement);
        });

        // Add event listeners to the remove buttons
        document.querySelectorAll(".remove-task").forEach(button => {
          button.addEventListener("click", function () {
            const taskId = this.getAttribute("data-id");
            removeTask(taskId);
          });
        });
      });
  }

  // Add a new task
  addTaskButton.addEventListener("click", function () {
    const taskTitle = newTaskInput.value.trim();
    if (taskTitle) {
      fetch("http://127.0.0.1:8000/api/tasks/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken, // Include CSRF token for POST requests
        },
        body: JSON.stringify({ title: taskTitle })
      })
        .then(response => response.json())
        .then(() => {
          newTaskInput.value = ""; // Clear input field
          loadTasks(); // Reload tasks after adding one
        })
        .catch(error => console.error("Error adding task:", error));
    }
  });

  // Function to remove a task
  function removeTask(taskId) {
    fetch(`http://127.0.0.1:8000/api/tasks/${taskId}/`, {
      method: "DELETE",
      headers: {
          "X-CSRFToken": csrfToken,  // CSRF token included
      },
      credentials: 'same-origin'  // Include cookies (CSRF cookie) with the request
    })
    .then(response => {
      if (response.ok) {
          loadTasks();  // Reload tasks after successful deletion
      } else {
          console.error("Failed to delete task:", response.statusText);
      }
    })
    .catch(error => console.error("Error removing task:", error));
  
  }

  // Load tasks when the popup is opened
  loadTasks();
});
