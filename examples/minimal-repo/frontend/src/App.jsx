import { clsx } from 'clsx';
import ContactForm from './components/ContactForm';

export default function App() {
  return (
    <div className={clsx('app', 'container')}>
      <h1>Contact us</h1>
      <ContactForm />
    </div>
  );
}
