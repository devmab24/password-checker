'use client'

import styles from './styles.module.css'
import { Container, Box, Flex } from '@chakra-ui/react'
import { InView } from 'react-intersection-observer';
import { useInView } from 'react-intersection-observer';
import DisplayInView from './CardAnimate/page';

function Main() {

    const { ref, inView } = useInView()
    const { ref: myRef, inView: myElementIsVisible } = useInView();
    const { ref: magicSectionRef, inView: magicSectionIsVisible } = useInView();
  
    return (
        <Container overflowX='hidden' maxW='100vw' bg='blue.600' centerContent>
            <Flex align='center' px={10} flexDir={'column'} padding='4' bg='blue.200' color='black' maxW='container.lg'>
                <Box px={20} fontSize={'1.5em'}>
                    There are many benefits to a joint design and development system. Not only
                    does it bring benefits to the design team, but it also brings benefits to
                    engineering teams. It makes sure that our experiences have a consistent look
                    and feel, not just in our design specs, but in production.
                </Box>
                <Box py={10}>
                    <h1 className={styles.title}>
                        Let&rsquo;s  Scroll
                    </h1>

                    <p className={styles.subtitle}>
                        devmab tutorials that will bring you joy!
                    </p>
                </Box>
                <Box py={10} className={styles.list}>
                    <h2 className={styles.heading}>
                        Guides?
                    </h2>

                    <ul className={styles.posts}>
                        <li>
                        <a href="https://www.npmjs.com/package/react-intersection-observer">
                            Check out more examples from React Instersecion Observer npm
                        </a>
                        </li>
                        <li>
                        <a href="https://chakra-ui.com/docs/components/">
                            ChakraUI-For User Friendly designs
                        </a>
                        </li>
                        <li>
                        <a href="https://chakra-ui.com/docs/components/">
                            see more....
                        </a>
                        </li>
                    </ul>
                </Box>
                <Box py={10}>
                    <h2 className={styles.heading}>
                        It&apos;s nice to be cool
                    </h2>

                    <p>There can be something cool here too.</p>
                </Box>
                
                <Box>
                    <DisplayInView />
                </Box>
                
                <Box>
                    <h2 ref={magicSectionRef} className={styles.heading}>
                        Magic 🪄
                    </h2>

                    <p>
                        <span className={`${styles.rocket} ${magicSectionIsVisible ? styles.animateRocket : ''}`}>
                        🚀
                        </span>
                    </p>
                </Box>
                <Box>
                    <h2 ref={myRef} className={styles.heading}>
                        Only Visible When IsInView... 🧐
                    </h2>

                    <p>{ myElementIsVisible ? 'Yes! 🥳' : 'No 🙈' }</p>
                </Box>
                <Box>
                    <div ref={ref}>
                        <h2>{`Header inside viewport ${inView}.`}</h2>
                    </div>
                </Box>
                <Box>
                <InView>
                    {({ inView, ref, entry }) => (
                    <div ref={ref}>
                        <h2>{`We're Using InView as a component ${inView}.`}</h2>
                    </div>
                    )}
                </InView>
                </Box>
            </Flex>

        </Container>
    )
}

export default Main