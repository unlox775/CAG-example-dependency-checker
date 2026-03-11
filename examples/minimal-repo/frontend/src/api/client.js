import axios from 'axios';

const client = axios.create({
  baseURL: '/api',
  headers: { 'Content-Type': 'application/json' },
});

export async function submitContact(payload) {
  const { data } = await client.post('/contact', payload);
  return data;
}
