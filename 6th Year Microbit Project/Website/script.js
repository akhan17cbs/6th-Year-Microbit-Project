// Your web app's Firebase configuration
var firebaseConfig = {
  apiKey: "AIzaSyC9wuM7frXED9TkW9Md0R9UF3s0-Eqxod0",
  authDomain: "test1-a59b2.firebaseapp.com",
  databaseURL: "https://test1-a59b2-default-rtdb.firebaseio.com",
  projectId: "test1-a59b2",
  storageBucket: "test1-a59b2.appspot.com",
  messagingSenderId: "933636733917",
  appId: "1:933636733917:web:c8a1f12b4e8aa8bcae1434"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

// Display LED
function addCommand(){
  var trafficLight = document.getElementById("commandIn").value;
  var today = new Date();
  var date = today.getFullYear() + '' + (today.getMonth()+1) + '' + today.getDate();
  var time = today.getHours() + '' + today.getMinutes() + '' + today.getSeconds();
  var dateTime = date + '' + time;

  var rootRef = firebase.database().ref();
  var storesRef = rootRef.child('/Commands/command/');
  var newStoreRef = storesRef.push();
  newStoreRef.set(
    {
      command: trafficLight,
      Timestamp: dateTime
    }
  );
  alert("Command sent...");
}

// Display Temperature
var myTemp = [];
var myfireb_connect = firebase.database().ref('/temperature/temp');

myfireb_connect.on("child_added", function(data, prevChildKey) {
  
  var dataPoint = data.val();
  myTemp.push(dataPoint.Temp);
  var totalT = 0;
  var i = 0;
  
  for(i = 0; i < myTemp.length; i++){
    totalT += myTemp[i];
  }
  
  var avg = totalT / myTemp.length;
  
  document.getElementById("avgL").innerHTML = avg;
  document.getElementById("liveL").innerHTML = myTemp[myTemp.length - 1];
});
