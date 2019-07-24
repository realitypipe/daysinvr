const getAPIUrl = () => {
  const url = window.location.href;
  if (url.includes('localhost')) {
    return 'https://api.staging.remixvr.org';
  } else if (url.includes('staging--remixvr')) {
    return 'https://api.staging.remixvr.org';
  } else {
    return 'https://api.remixvr.org';
  }
};

export default getAPIUrl;
