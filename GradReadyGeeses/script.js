async function fetchCourseData() {
    try {
        const response = await fetch('result.json');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error("Could not fetch course data:", error);
        return null;
    }
}

function addCourse(sectionId, courseName) {
    const section = document.getElementById(sectionId);
    const courseElement = document.createElement('div');
    courseElement.className = 'course';
    courseElement.innerHTML = `
        <span>${courseName}</span>
        <a href="https://ucalendar.uwaterloo.ca/1920/COURSE/course-CS.html#CS240" target="_blank" class="course-icon">
            <img src="attach.png" alt="Attach" class="attach-icon">
        </a>
    `;
    section.appendChild(courseElement);
}

function addCourseGroup(sectionId, courses) {
    const courseString = courses.join(' or ');
    addCourse(sectionId, courseString);
}

function updateCoursesNeeded(number) {
    document.getElementById('coursesNeeded').textContent = number;
}

async function populateCourses() {
    const courseData = await fetchCourseData();
    
    if (!courseData) {
        console.error("Failed to load course data");
        return;
    }

    // ADD ALL COURSES TO EACH GROUP 

    courseData.list_1.forEach(group => {
        addCourseGroup('table1Courses', group);
    });


    courseData.major_requirements.forEach(group => {
        addCourseGroup('majorSpecificCourses', group);
    });

    // Calculate total number of courses needed
    const totalCourses = courseData.list_1.length + courseData.major_requirements.length;
    updateCoursesNeeded(totalCourses);
}

// Call this function when the page loads
document.addEventListener('DOMContentLoaded', populateCourses);