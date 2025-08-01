
// Mobile Navigation Toggle
document.addEventListener('DOMContentLoaded', function() {
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            navToggle.classList.toggle('active');
        });
    }

    // Close mobile menu when clicking on a link
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            navMenu.classList.remove('active');
            navToggle.classList.remove('active');
        });
    });
});

// Task Management Functions
let taskToDelete = null;

// Delete Task Functions
// function confirmDelete(taskId) {
//     taskToDelete = taskId;
//     const modal = document.getElementById('deleteModal');
//     if (modal) {
//         modal.style.display = 'block';
//     }
// }

// function closeDeleteModal() {
//     const modal = document.getElementById('deleteModal');
//     if (modal) {
//         modal.style.display = 'none';
//     }
//     taskToDelete = null;
// }

// function deleteTask() {
//     if (taskToDelete) {
//         // In a real application, this would make an AJAX call to delete the task
//         console.log('Deleting task with ID:', taskToDelete);
        
//         // Simulate task deletion
//         alert('Task deleted successfully!');
        
//         // Redirect to dashboard
//         window.location.href = '/dashboard/';
//     }
//     closeDeleteModal();
// }

// Mark Task as Completed
function markAsCompleted(taskId) {
    // In a real application, this would make an AJAX call to update the task status
    console.log('Marking task as completed:', taskId);
    
    // Simulate task completion
    alert('Task marked as completed!');
    
    // Redirect to dashboard
    window.location.href = '/dashboard/';
}

// Form Validation
function validateTaskForm() {
    const title = document.getElementById('title');
    const dueDate = document.getElementById('due_date');
    const priority = document.getElementById('priority');
    const status = document.getElementById('status');
    
    let isValid = true;
    
    // Reset previous error states
    const inputs = [title, dueDate, priority, status];
    inputs.forEach(input => {
        if (input) {
            input.style.borderColor = '#e2e8f0';
        }
    });
    
    // Validate required fields
    if (title && !title.value.trim()) {
        title.style.borderColor = '#ef4444';
        isValid = false;
    }
    
    if (dueDate && !dueDate.value) {
        dueDate.style.borderColor = '#ef4444';
        isValid = false;
    }
    
    if (priority && !priority.value) {
        priority.style.borderColor = '#ef4444';
        isValid = false;
    }
    
    if (status && !status.value) {
        status.style.borderColor = '#ef4444';
        isValid = false;
    }
    
    return isValid;
}

// Add form validation to task forms
// document.addEventListener('DOMContentLoaded', function() {
//     const taskForms = document.querySelectorAll('.task-form');
//     taskForms.forEach(form => {
//         form.addEventListener('submit', function(e) {
//             if (!validateTaskForm()) {
//                 e.preventDefault();
//                 alert('Please fill in all required fields.');
//             }
//         });
//     });
// });

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Add loading states to buttons
function addLoadingState(button) {
    const originalText = button.innerHTML;
    button.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Loading...';
    button.disabled = true;
    
    // Simulate loading (remove this in real implementation)
    setTimeout(() => {
        button.innerHTML = originalText;
        button.disabled = false;
    }, 2000);
}

// Add click handlers for form submissions
// document.addEventListener('DOMContentLoaded', function() {
//     const submitButtons = document.querySelectorAll('button[type="submit"]');
//     submitButtons.forEach(button => {
//         button.addEventListener('click', function(e) {
//             e.preventDefault()
//             if (validateTaskForm()) {
//                 addLoadingState(this);
//             }
//         });
//     });
// });

// Close modal when clicking outside
window.addEventListener('click', function(event) {
    const modal = document.getElementById('deleteModal');
    if (event.target === modal) {
        closeDeleteModal();
    }
});

// Keyboard navigation for modals
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        closeDeleteModal();
    }
});

// Add animation classes on scroll
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe elements for animation
document.addEventListener('DOMContentLoaded', function() {
    const animateElements = document.querySelectorAll('.feature-card, .task-card');
    animateElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
});

console.log('TaskHero JavaScript loaded successfully!');
