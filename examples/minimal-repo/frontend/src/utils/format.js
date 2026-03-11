import { format, formatDistanceToNow } from 'date-fns';

export function formatTimestamp(ts) {
  return format(new Date(ts), 'MMM d, yyyy HH:mm');
}

export function formatRelative(ts) {
  return formatDistanceToNow(new Date(ts), { addSuffix: true });
}
