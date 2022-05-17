#!/usr/bin/node
// Script that computes number of task completed by user

const request = require('request');
const urlAPI = process.argv[2];

request(urlAPI, (error, res, content) => {
  if (error) {
    console.error(error);
    return;
  }

  const taskList = JSON.parse(content);
  const completedTasks = {};

  for (const task of taskList) {
    if (task.completed) {
      const userID = task.userId;
      completedTasks[userID] = (completedTasks[userID] + 1 || 1);
    }
  }
  console.log(completedTasks);
});
