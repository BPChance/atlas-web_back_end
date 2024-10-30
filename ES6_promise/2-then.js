function handleResponseFromAPI(promise) {
  return promise
    .then(() => {
      return { status: 200, body: 'Success' };
    })
    .catch(() => {
      return new Error();
    })
    .finally(() => {
      console.log('Got a response from the API');
    });
}

export default handleResponseFromAPI;
