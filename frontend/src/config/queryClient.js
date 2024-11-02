import { QueryClient } from "@tanstack/react-query";
import { useAuthenticatedRequest } from "@/hooks/useAuthenticatedRequest";

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 5 * 60 * 1000,
      cacheTime: 5 * 60 * 1000,
      refetchOnWindowFocus: true,
    },
  },
});

export default queryClient;
