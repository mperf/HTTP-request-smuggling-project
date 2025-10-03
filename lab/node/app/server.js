// const express = require('express');
// const app = express();

// // Middleware to handle raw requests - important for smuggling detection
// app.use(express.raw({ type: '*/*', limit: '10mb' }));

// // Log all incoming requests
// app.use((req, res, next) => {
//     console.log('=== Backend Request ===');
//     console.log('Method:', req.method);
//     console.log('URL:', req.url);
//     console.log('Headers:', JSON.stringify(req.headers, null, 2));
//     console.log('Body length:', req.body ? req.body.length : 0);
//     console.log('========================');
//     next();
// });

// // Simple authentication endpoint
// app.get('/admin', (req, res) => {
//    res.json({ message: 'Welcome to the admin area' });
// });

// // Public endpoint
// app.get('/public', (req, res) => {
//     res.json({ message: 'This is a public endpoint' });
// });

// // Catch-all route
// app.all('*', (req, res) => {
//     res.json({ 
//         message: 'Backend received request',
//         method: req.method,
//         url: req.url,
//         timestamp: new Date().toISOString()
//     });
// });

// const PORT = process.env.PORT || 3000;
// app.listen(PORT, () => {
//     console.log(`Backend server running on port ${PORT}`);
//     console.log('Ready to receive requests...');
// });

const http = require('http');

const server = http.createServer((req, res) => {
    console.log('=== Backend Request ===');
    console.log('Method:', req.method);
    console.log('URL:', req.url);
    console.log('Headers:', JSON.stringify(req.headers, null, 2));
    
    let body = '';
    req.on('data', chunk => {
        body += chunk.toString();
    });
    
    req.on('end', () => {
        console.log('Body:', body);
        console.log('========================');
        
        if (req.url === '/admin') {
            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ message: 'Admin access granted!' }));
        } else if (req.url === '/postComment' && req.method === 'POST') {
            const socialPost = body.trim();
            console.log('Social post:', socialPost);
            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ message: `message has been posted: ${socialPost}` }));
        } else if (req.url === '/deleteAccount' && req.method === 'POST') {
            const auth = req.headers['authorization'];
            if (auth && auth.startsWith('Basic ')) {
            const base64 = auth.split(' ')[1];
            const decoded = Buffer.from(base64, 'base64').toString();
            const accountName = decoded.split(':')[0];
            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ message: `${accountName} user has been deleted!` }));
            } else {
            res.writeHead(401, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ message: 'Unauthorized' }));
            }
        } else {
            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ message: 'Public endpoint' }));
        }
    });
});

server.listen(3000, () => {
    console.log('Backend server running on port 3000');
});
