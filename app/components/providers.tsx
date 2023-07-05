'use client'

import { CacheProvider } from '@chakra-ui/next-js'
import { ChakraProvider, theme } from '@chakra-ui/react'
import { Rubik } from 'next/font/google';

const rubik = Rubik({ subsets: ['latin'] });

    <style jsx global>
      {`
        :root {
          --font-rubik: ${rubik.style.fontFamily};
        }
      `}
    </style>

export function Providers({ 
    

    children 
  }: { 
  children: React.ReactNode 
  }) {
  return (
    <CacheProvider>
      <ChakraProvider theme={theme}>
        {children}
      </ChakraProvider>
    </CacheProvider>
  )
}