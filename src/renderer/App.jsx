import React, { useState } from 'react';
import ContentLoader from './ContentLoader';

const App = () => {
    const [page, setPage] = useState('tools');

    return (
        <div>
            <h1>Electron + Vite + React</h1>
            <button onClick={() => setPage('tools')}>Tools</button>
            <button onClick={() => setPage('safety')}>Safety</button>
            <button onClick={() => setPage('test')}>test</button>
            <div id="content">
                <ContentLoader page={page} />
            </div>
        </div>
    )
}

export default App;