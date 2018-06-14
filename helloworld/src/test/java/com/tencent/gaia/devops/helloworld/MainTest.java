package com.tencent.gaia.devops.helloworld; 

import org.junit.Test; 
import org.junit.Before; 
import org.junit.After;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

/** 
* Main Tester. 
* 
* @author <Authors name> 
* @since <pre>五月 30, 2018</pre> 
* @version 1.0 
*/ 
public class MainTest { 

@Before
public void before() throws Exception {
    System.out.println("unittest begin");
} 

@After
public void after() throws Exception { 
} 

/** 
* 
* Method: main(String[] arg) 
* 
*/ 
@Test
public void testMain() throws Exception { 
    assertTrue(6 == 6);
} 

/** 
* 
* Method: handle(HttpExchange exchange) 
* 
*/ 
@Test
public void testHandle() throws Exception {
    assertEquals("test", "test");
} 


} 
