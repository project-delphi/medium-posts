const mediumToMarkdown = require('medium-to-markdown');
const request = require('request');
const fs = require('fs');

mediumToMarkdown.convertFromUrl('https://medium.com/@ravikalia/simple-pca-implementations-7edb130fb01b')
.then( (markdown) => {
  console.log(markdown)
  fs.writeFile('./docs/simple-pca-implementations.md', markdown, (err) => {  
      if (err) throw err;
      // success case, the file was saved
      console.log('markdown saved!');
  });
});

// request('https://api.medium.com/v1/users/@ravikalia/publications', { json: true }, (err, res, body) => {
//   if (err) { 
//     console.log('Here is an error')  
//     return console.log(err); 
// }
//   console.log('processing body')
//   console.log(body);
//   console.log(body.explanation);
// });


