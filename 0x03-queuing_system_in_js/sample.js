import redis from 'redis';

const client = redis.createClient();


client.on('error', (err) => console.log(`user is not connected: ${err}`));

client.on('connect', () =>{
    console.log(`redis client connected to server`)
}).on('error', (err) => {
    console.log(`reddit user not connected:${err}`)
});

function setnewschool (school, value) {
    client.set(school, value, (error, response)=>{
        redis.print(`reply, ${response}`);
    });
}

const displayschoolval = async(school) => {
    try{
        const reply = await getasync(school);
        console.log(reply);
    }
    catch (error){
        console.log(`error retrieving value for ${school}: ${error.message}`);
    }
};
setnewschool('klausschool, 100');
displayschoolval('klausschool');
