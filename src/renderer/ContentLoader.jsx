import React, { useEffect, useState } from 'react';

const ContentLoader = ({ page }) => {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');

    useEffect(() => {
        setLoading(true);
        setError('');

        let url;
        if (page === 'tools') {
            url = 'http://localhost:5000/api/tools';
        } else if (page === 'safety') {
            url = 'http://localhost:5000/api/safety';
        } else if (page === 'test') {
            url = 'http://localhost:5000/api/test';
        } else {
            setError('Invalid page');
            setLoading(false);
            return;
        }

        fetch(url)
            .then((res) => res.json())
            .then((json) => {
                setData(json);
                setLoading(false);
            })
            .catch((err) => {
                console.error(err);
                setError('Error loading data');
                setLoading(false);
            });
    }, [page]);

    if (loading) return <p>Loading...</p>;
    if (error) return <p>{error}</p>;

    return (
        <div>
            <h2>{page}</h2>
            {data.map((item, index) => (
                <p key={index}>
                    {(item.name || item.tip)}: {(item.use || item.description)}
                </p>
            ))}
        </div>
    )
}

export default ContentLoader;