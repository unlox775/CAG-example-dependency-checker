import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import { format } from 'date-fns';
import { v4 as uuidv4 } from 'uuid';
import { debounce } from 'lodash';
import { submitContact } from '../api/client';

const schema = z.object({
  name: z.string().min(1, 'Name required'),
  email: z.string().email('Invalid email'),
  message: z.string().min(10, 'Message too short'),
});

export default function ContactForm() {
  const { register, handleSubmit, formState: { errors } } = useForm({
    resolver: zodResolver(schema),
  });

  const onSubmit = debounce(async (data) => {
    const payload = { id: uuidv4(), ...data, submittedAt: format(new Date(), 'yyyy-MM-dd HH:mm') };
    await submitContact(payload);
  }, 300);

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register('name')} placeholder="Name" />
      {errors.name && <span>{errors.name.message}</span>}
      <input {...register('email')} type="email" placeholder="Email" />
      {errors.email && <span>{errors.email.message}</span>}
      <textarea {...register('message')} placeholder="Message" />
      {errors.message && <span>{errors.message.message}</span>}
      <button type="submit">Send</button>
    </form>
  );
}
