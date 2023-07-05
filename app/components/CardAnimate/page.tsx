'use client'

import styles from './style.module.css';
import { useInView } from 'react-intersection-observer';
import { Card, CardBody, CardHeader, Center, HStack } from '@chakra-ui/react';
// import { useEffect, useRef, useState } from 'react';

const DisplayInView = () => {

    const { ref: myRef, inView: myElementIsVisible } = useInView();
   
    return (
        <>
            <div className={styles.cardContainer}>
                <div ref={myRef} className={`${styles.hiddenCard} ${myElementIsVisible ? styles.show : ''} `}>
                    <Center>
                        <HStack align="center" gap={5}>
                            <Card className={styles.cardContent} maxW="10em" textAlign={'center'}>
                                <CardHeader>
                                    <h2>Card Header</h2>
                                </CardHeader>
                                <CardBody>
                                    Lorem, ipsum dolor sit amet consectetur adipisicing elit.
                                </CardBody>
                            </Card>
                            <Card className={styles.cardContent} maxW="10em" textAlign={'center'}>
                                <CardHeader>
                                    <h2>Card Header</h2>
                                </CardHeader>
                                <CardBody>
                                    Lorem, ipsum dolor sit amet consectetur adipisicing elit.
                                </CardBody>
                            </Card>
                            <Card className={styles.cardContent} maxW="10em" textAlign={'center'}>
                                <CardHeader>
                                    <h2>Card Header</h2>
                                </CardHeader>
                                <CardBody>
                                    Lorem, ipsum dolor sit amet consectetur adipisicing elit.
                                </CardBody>
                            </Card>
                            <Card className={styles.cardContent} maxW="10em" textAlign={'center'}>
                                <CardHeader>
                                    <h2>Card Header</h2>
                                </CardHeader>
                                <CardBody>
                                    Lorem, ipsum dolor sit amet consectetur adipisicing elit.
                                </CardBody>
                            </Card>
                        </HStack>
                        </Center>
                </div>
            </div>
        </>
    );
};

export default DisplayInView;