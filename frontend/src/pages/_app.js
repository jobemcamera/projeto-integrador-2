import "@/styles/globals.css";
import theme from "@/config/theme";
import { ThemeProvider } from "@mui/material";
import { QueryClientProvider } from "@tanstack/react-query";
import queryClient from "@/queryClient";
import Head from "next/head";

export default function App({ Component, pageProps }) {
  return (
    <QueryClientProvider client={queryClient}>
      <ThemeProvider theme={theme}>
        <Head>
          <title>Controle de estoque</title>
          <meta name="description" content="Generated by create next app" />
          <meta name="viewport" content="width=device-width, initial-scale=1" />
          <link rel="icon" href="/loja.png" />
        </Head>
        <Component {...pageProps} />
      </ThemeProvider>
    </QueryClientProvider>
  );
}
