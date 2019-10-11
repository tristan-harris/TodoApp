// toggles the one class
function toggleClass(element, _class) {
    if(element.classList.contains(_class)) {
        element.classList.remove(_class);
    } else {
        element.classList.add(_class);
    }
}

// toggles betwen two different classes
function swapClass(element, class_1, class_2) {
    toggleClass(element, class_1);
    toggleClass(element, class_2);
}

function sendJSON(address, the_data) {

    fetch(address, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(the_data),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    }).then(function(response) {

        if(response.status !== 200) {
            console.error(`ERROR [status!=200]: Response status -> ${response.status}`);
            return ;
        }

        response.json().then(function(data) {
            console.log(data);
        })
        
    });
}


function crossTodo(todo_task_id) {
    const the_card = document.querySelector('.todo-card[data-todo-task-id="' + todo_task_id + '"]');
    const tick_icon = the_card.querySelector('.todo-tick-button-icon');
    const todo_title = the_card.querySelector('.todo-title');

    swapClass(tick_icon, 'fa-square', 'fa-check-square');
    swapClass(tick_icon, 'far', 'fas');
    toggleClass(todo_title, 'todo-title-completed');

    const the_card_completed_status = tick_icon.classList.contains('fa-check-square');
    const request_data = {
        "todo-id": todo_task_id,
        "todo-completed": the_card_completed_status
    };
    sendJSON('/completed', request_data)
}

function deleteTodo(todo_task_id) {
    const the_card = document.querySelector('.todo-card[data-todo-task-id="' + todo_task_id + '"]');
    the_card.style.opacity = '0';
    the_card.classList.add('card-fade-out');

    // removes the_card from the DOM after 500ms
    setTimeout(function(){the_card.remove();}, 500);

    sendJSON('/delete', {"todo-id": todo_task_id});
}

function createNewTodo() {
    const todo_title = document.getElementById("new-todo-content").value;
    sendJSON('/create', {"todo-title": todo_title});
}

function newTodoTask() {
    const new_todo_task = document.getElementById('new-todo-task');
    const new_todo_button = document.querySelector('.new-todo-button');

    new_todo_task.style.display = "flex";
    new_todo_button.style.display = "none";

    const new_todo_task_input = new_todo_task.querySelector('#new-todo-content');
    new_todo_task_input.focus();
}

function checkNewTodoFocus() {
    const new_todo_task = document.getElementById('new-todo-task');
    const new_todo_task_input = new_todo_task.querySelector('#new-todo-content');
    const new_todo_task_submit = new_todo_task.querySelector('#new-todo-submit');
    
    // needs to be a timer between switching focus, because active element gets set to the body inbetween switch
    setTimeout(function()
    {
        console.log(document.activeElement);
        if(document.activeElement !== new_todo_task_input && document.activeElement !== new_todo_task_submit) 
        {
            const new_todo_button = document.querySelector('.new-todo-button');
            new_todo_task_input.value = "";
            new_todo_task.style.display = "none";
            new_todo_button.style.display = "block";
        }
    }, 100);
}
