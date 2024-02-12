// src/pages/page.js

import React from 'react';
import axios from 'axios';

const Page = ({ posts }) => {
  return (
    <div>
      <h1>Hello Next.js</h1>
      {/* Display posts from the FastAPI backend */}
      <ul>
        {posts.map((post) => (
          <li key={post.id}>{post.title}</li>
        ))}
      </ul>
    </div>
  );
};

export async function getServerSideProps() {
  // Fetch posts from the FastAPI backend
  const response = await axios.get('http://localhost:8000/api/posts');
  const posts = response.data;

  return {
    props: {
      posts,
    },
  };
}

export default Page;
