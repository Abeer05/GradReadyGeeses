document.addEventListener('DOMContentLoaded', () => {
    fetch('results.json')
      .then(response => response.json())
      .then(data => {
        const eligibleContainer = document.querySelector('.eligible-container');
        const notEligibleContainer = document.querySelector('.not-eligible-container');
  
        if (data.list_1.length === 0 && data.major_requirements.length === 0) {
          eligibleContainer.style.display = 'block';
        } else {
          notEligibleContainer.style.display = 'block';
          document.getElementById('coursesNeeded').textContent = data.list_1.length + data.major_requirements.flat().length;
  
          const majorSpecificCourses = document.getElementById('majorSpecificCourses');
          const table1Courses = document.getElementById('table1Courses');
  
          data.major_requirements.flat().forEach(course => {
            const courseElement = document.createElement('div');
            courseElement.className = 'course';
            courseElement.textContent = course;
            majorSpecificCourses.appendChild(courseElement);
          });
  
          data.list_1.flat().forEach(course => {
            const courseElement = document.createElement('div');
            courseElement.className = 'course';
            courseElement.textContent = course;
            table1Courses.appendChild(courseElement);
          });
        }
      })
      .catch(error => console.error('Error fetching JSON:', error));
  });
  