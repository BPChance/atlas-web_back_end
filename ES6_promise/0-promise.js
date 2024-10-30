function getResponseFromApi() {
  return new Promise((resolve, reject) => {
    const success = true;

    if (success) {
      resolve('Yayyy!');
    } else {
      reject(new Error('Failed to get response.'));
    }
  });
}

export default getResponseFromApi;
