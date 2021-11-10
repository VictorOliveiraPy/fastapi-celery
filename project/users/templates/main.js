<script>
  function update_progress(yourForm, task_id, btnHtml) {
    fetch(`/users/task_status/?task_id=${task_id}`, {
      method: 'GET',
    })
      .then(response => response.json())
      .then((res) => {
        const taskStatus = res.state;

        if (taskStatus !== 'PENDING' && taskStatus !== 'PROGRESS') {
          const msg = yourForm.querySelector('#messages');
          const submitBtn = yourForm.querySelector('button[type="submit"]');

          if (taskStatus === 'SUCCESS') {
            msg.innerHTML = 'job succeeded';
          } else if (taskStatus === 'FAILURE') {
            // display error message on the form
            msg.innerHTML = res.error;
          }

          submitBtn.disabled = false;
          submitBtn.innerHTML = btnHtml;
        } else {
          // the task is still running
          setTimeout(function() {
            update_progress(yourForm, task_id, btnHtml);
          }, 1000);
        }
      })
      .catch((error) => {
          console.error('Error:', error)
        }
      );
  }

  function serialize(data) {
    let obj = {};
    for (let [key, value] of data) {
      if (obj[key] !== undefined) {
        if (!Array.isArray(obj[key])) {
          obj[key] = [obj[key]];
        }
        obj[key].push(value);
      } else {
        obj[key] = value;
      }
    }
    return obj;
  }

  document.addEventListener("DOMContentLoaded", function() {
    const yourForm = document.getElementById("your-form");
    yourForm.addEventListener("submit", function(event) {
      event.preventDefault();
      const submitBtn = yourForm.querySelector('button[type="submit"]');
      const btnHtml = submitBtn.innerHTML;
      const spinnerHtml = 'Processing...';
      submitBtn.disabled = true;
      submitBtn.innerHTML = spinnerHtml;

      const msg = yourForm.querySelector('#messages');
      msg.innerHTML = '';

      // Get all field data from the form
      let data = new FormData(yourForm);
      // Convert to an object
      let formData = serialize(data);

      fetch('/users/form/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData),
      })
        .then(response => response.json())
        .then((res) => {
          // after we get Celery task id, we start polling
          const task_id = res.task_id;
          update_progress(yourForm, task_id, btnHtml);
          console.log(res);
        })
        .catch((error) => {
            console.error('Error:', error)
          }
        );
    });
  });
</script>