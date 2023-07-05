import Footer from './components/Footer'
import Navbar from './components/Navbar'
import { Providers } from './components/providers'
import './globals.css'
import { Inter } from 'next/font/google'

const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: 'Scrolling App',
  description: 'Learning react-Intersection-Observer',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <Providers>
          <Navbar />
        { children}
        <Footer />
        </Providers>
      </body>
    </html>
  )
}
