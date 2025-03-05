import kue from 'kue';

const queue = kue.createQueue();

// handle notifs
function sendNotifications(phoneNumber, message) {
  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`
  );
}

queue.process('push_notification_code', (job, done) => {
  sendNotifications(job.data.phoneNumber, job.data.message);
  done();
});
