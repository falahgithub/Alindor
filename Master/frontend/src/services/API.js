const API_URL = 'http://alindor-env.eba-j2su4ewx.us-east-1.elasticbeanstalk.com/upload'; 

const uploadAudio = async (file) => {
  const formData = new FormData();
  formData.append('audio_file', file);

  try {
    const response = await fetch(API_URL, {
      method: 'POST',
      body: formData,
    });

    if (!response.ok) {
      throw new Error(`API request failed with status ${response.status}`);
    }

    const data = await response.json();
 

    return data;
  } catch (error) {
    console.error('Error uploading audio:', error);
    throw error; 
  }
};

export {uploadAudio} ;
