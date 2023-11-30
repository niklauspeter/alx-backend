import redis from 'redis';
import util from 'util'; // Import the util module


const client = redis.createClient();

// client = redis.createClient();

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));

client.on('connect', () => {
    console.log('Redis client connected to the server');
}).on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (error, response) => {
        redis.print(`Reply: ${response}`);
    });
}
const displaySchoolValue = (schoolName, callback) => {
    getAsync(schoolName)
        .then(result => {
            console.log(result);
            callback(null, result); // Pass the result to the callback
        })
        .catch(error => {
            console.error(`Error retrieving value for ${schoolName}: ${error.message}`);
            callback(error, null); // Pass the error to the callback
        });
};
// let displaySchoolValue = async (schoolName) => {
//     try {
//         const result = await getAsync(schoolName);
//         console.log(result);
//     } catch (error) {
//         console.error(`Error retrieving value for ${schoolName}: ${error.message}`);
//     }
// };
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
