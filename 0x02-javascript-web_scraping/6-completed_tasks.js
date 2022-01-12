#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const taskList = JSON.parse(body);
  const completedList = {};
  for (let i = 0; i < taskList.length; i++) {
    if (taskList[String(i)].completed) {
      if (!completedList[String(taskList[String(i)].userId)]) {
        completedList[String(taskList[String(i)].userId)] = 0;
      }
      completedList[String(taskList[String(i)].userId)]++;
    }
  }
  console.log(completedList);
});
