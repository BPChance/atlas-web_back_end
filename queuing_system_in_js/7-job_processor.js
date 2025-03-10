import kue from 'kue';

const queue = kue.createQueue();

const blackListedNumbers = ['4153518780', '4153518781'];

// process notifs
function sendNotifications(phoneNumber, message, job, done) {
  job.progress(0, 100);

  if (blackListedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  job.progress(50, 100);
  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`
  );

  done();
}

queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotifications(job.data.phoneNumber, job.data.message, job, done);
});
