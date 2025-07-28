export type TLog = {
  id: string;
  timestamp: string;
  level: string;
  message: string;
  service: string;
}

// Les valeurs peuvent etre nulles
export type TSearchLog = {
  q?: string;
  level?: string;
  service?: string;
}

export type TSendLog = {
  level: string;
  message: string;
  service: string;
}
