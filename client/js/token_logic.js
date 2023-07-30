// URLs of the encoder files
const encoderJsonUrl = 'https://cdn.discordapp.com/attachments/400300649562243093/1135340649089073282/encoder.json';
const vocabBpeUrl = 'https://cdn.discordapp.com/attachments/400300649562243093/1135340648808058990/vocab.bpe';

// Fetch the encoder files
const encoderPromise = fetch(encoderJsonUrl).then(response => response.json());
const vocabPromise = fetch(vocabBpeUrl).then(response => response.text());

Promise.all([encoderPromise, vocabPromise]).then(([encoder, vocab]) => {
  // Initialize the Encoder with the fetched data
  const enc = new Encoder(encoder, vocab);

  // Now you can use the Encoder
  const tokens = enc.encode('Hello, world!');
  console.log(tokens);
});
