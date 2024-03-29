import axios from 'axios';

const locale = document.documentElement.lang;
const getMessages = async(limit, skip) => {
    try {
        const response = await axios.get(`http://thoughty-app.com/${locale}/lobby/get?limit=${limit}&skip=${skip}`);
        return response.data;
    } catch(error) {
        console.log(error)
    }
};

export default getMessages;