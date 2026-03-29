const API_URL = "https://ai-journal-system-2sc8.onrender.com";
async function submitJournal(){

let text = document.getElementById("entry").value;

if(text.trim() === ""){
alert("Please write something");
return;
}

document.getElementById("result").innerText = "Analyzing...";

try{

let response = await fetch(`${API_URL}/journal`,{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({text:text})
});

let data = await response.json();

document.getElementById("result").innerText =
"Emotion: " + data.emotion;

loadHistory();
loadChart();

}catch(error){

document.getElementById("result").innerText =
"Server connection error";

}

}



async function loadHistory(){

let response = await fetch(`${API_URL}/journals`);

let data = await response.json();

let list = document.getElementById("history");

list.innerHTML = "";

data.forEach(entry => {

let li = document.createElement("li");

li.innerText = entry[1] + " → " + entry[2];

list.appendChild(li);

});

}



async function loadChart(){

let response = await fetch(`${API_URL}/journals`);

let data = await response.json();

let counts = {};

data.forEach(entry => {

let emotion = entry[2];

counts[emotion] = (counts[emotion] || 0) + 1;

});

let labels = Object.keys(counts);
let values = Object.values(counts);

const ctx = document.getElementById('emotionChart');

new Chart(ctx, {
type: 'bar',
data: {
labels: labels,
datasets: [{
label: 'Emotion Frequency',
data: values
}]
}
});

}


loadHistory();
loadChart();