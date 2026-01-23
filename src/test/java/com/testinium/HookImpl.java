package com.testinium;

import com.testinium.driver.TestiniumAndroidDriver;
import com.testinium.driver.TestiniumIOSDriver;
import com.testinium.selector.Selector;
import com.testinium.selector.SelectorFactory;
import com.testinium.selector.SelectorType;
import com.testinium.util.TestiniumEnvironment;
import com.thoughtworks.gauge.AfterScenario;
import com.thoughtworks.gauge.BeforeScenario;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.ios.IOSDriver;
import io.appium.java_client.remote.AndroidMobileCapabilityType;
import io.appium.java_client.remote.IOSMobileCapabilityType;
import io.appium.java_client.remote.MobileCapabilityType;
import io.appium.java_client.remote.MobilePlatform;
import org.apache.commons.lang3.StringUtils;
import org.openqa.selenium.NoSuchElementException;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.support.events.EventFiringWebDriver;
import org.openqa.selenium.support.ui.FluentWait;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.net.MalformedURLException;
import java.net.URL;
import java.time.Duration;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.TimeUnit;

import static com.testinium.util.Constants.CapabilityConstants.APPIUM_AUTO_GRANT_PERMISSIONS;


public class HookImpl {
    private Logger logger = LoggerFactory.getLogger(getClass());

    public static AppiumDriver driver;

    protected static FluentWait<AppiumDriver> appiumFluentWait;
    protected boolean localAndroid=false;
    public static boolean isDeviceAnd=true;
    protected static Selector selector ;
    protected URL hubUrl;


    @BeforeScenario
    public void beforeScenario() throws Exception {
        System.out.println("!!!!!!!!!!!!!!!!!!!!!!!!!!!Test baslıyor!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
        System.out.println("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
        if (StringUtils.isEmpty(System.getenv("key"))) {
            if (localAndroid) {
                isDeviceAnd=true;
                logger.info("Local Browser");
                DesiredCapabilities overridden = new DesiredCapabilities();

                overridden.setCapability(MobileCapabilityType.PLATFORM_NAME, MobilePlatform.ANDROID);
                overridden.setCapability("skipDeviceInitialization", true);
                overridden.setCapability("skipServerInstallation", true);
                overridden.setCapability("ignoreUnimportantViews", true);
                overridden.setCapability("waitForIdleTimeout",150);
                overridden.setCapability(MobileCapabilityType.DEVICE_NAME, "RFCY51GBYTL");
                //desiredCapabilities.setCapability(MobileCapabilityType.DEVICE_NAME, "device");
                overridden
                        .setCapability(AndroidMobileCapabilityType.APP_PACKAGE,
                                "com.gratis.android.dev");
                overridden
                        .setCapability(AndroidMobileCapabilityType.APP_ACTIVITY,
                                "com.gratis.android.GratisMainActivity");
                overridden.setCapability(MobileCapabilityType.AUTOMATION_NAME, "uiautomator2");
                overridden
                        .setCapability(MobileCapabilityType.NO_RESET, false);
                overridden
                        .setCapability(MobileCapabilityType.FULL_RESET, false);
                overridden.setCapability(MobileCapabilityType.NEW_COMMAND_TIMEOUT, 3000);
                overridden.setCapability("unicodeKeyboard", false);
                //desiredCapabilities.setCapability("resetKeyboard", true);
                URL url = new URL("http://127.0.0.1:4723/");
                driver = new AndroidDriver(url, overridden);

            } else {
                isDeviceAnd=false;
                DesiredCapabilities overridden = new DesiredCapabilities();
                overridden
                        .setCapability(MobileCapabilityType.PLATFORM_NAME, MobilePlatform.IOS);
                overridden.setCapability(MobileCapabilityType.AUTOMATION_NAME, "XCUITest");
                overridden.setCapability(MobileCapabilityType.UDID, "ca796f0c0ead8729c124b5bda73f8de53b4dec8a");
                overridden
                        .setCapability(IOSMobileCapabilityType.BUNDLE_ID, "com.gratis.ios");
                //setCapability(IOSMobileCapabilityType.BUNDLE_ID, "com.pharos.gratis.uat");
                overridden.setCapability(MobileCapabilityType.DEVICE_NAME, "devtestinium iPhone X");
                overridden.setCapability(MobileCapabilityType.PLATFORM_VERSION, "16.7.10");
                overridden.setCapability(MobileCapabilityType.NEW_COMMAND_TIMEOUT, 300);
                //desiredCapabilities.setCapability("autoAcceptAlerts", true);



                URL url = new URL("http://127.0.0.1:4723/");
                driver = new IOSDriver(url, overridden);


            }
        } else {

                System.out.println("isAndroid:" + TestiniumEnvironment.isPlatformAndroid());
                if(localAndroid || TestiniumEnvironment.isPlatformAndroid()){
                    DesiredCapabilities overridden = new DesiredCapabilities();;
                isDeviceAnd=true;
                overridden.setCapability("key", System.getenv("key"));
//                    overridden
//                        .setCapability(AndroidMobileCapabilityType.APP_PACKAGE,
//                                "com.gratis.android.dev");
//
//                    overridden
//                        .setCapability(AndroidMobileCapabilityType.APP_ACTIVITY,
//                                "com.gratis.android.GratisMainActivity");
                //    overridden.setCapability(MobileCapabilityType.AUTOMATION_NAME,"Uiautomator2");
                    //overridden.setCapability(MobileCapabilityType.AUTOMATION_NAME,"UiAutomator2");
                    overridden.setCapability(MobileCapabilityType.NO_RESET, false);
                    overridden.setCapability(MobileCapabilityType.FULL_RESET, false);
                    overridden.setCapability(APPIUM_AUTO_GRANT_PERMISSIONS, true);
                    overridden.setCapability("unicodeKeyboard", true);
                    overridden.setCapability("resetKeyboard", true);
                    overridden.setCapability("appium:settings[waitForIdleTimeout]",500);

                    overridden.setCapability("appium:[skipDeviceInitialization]",true);
                    overridden.setCapability("appium:[skipServerInstallation]",true);
                    overridden.setCapability("appium:[ignoreUnimportantViews]",true);
                    hubUrl = new URL("http://127.0.0.1:4723/");
                    driver = new TestiniumAndroidDriver(hubUrl,overridden);

                    driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);
                    appiumFluentWait = new FluentWait<AppiumDriver>(driver);
                    appiumFluentWait.withTimeout(Duration.ofSeconds(8))
                            .pollingEvery(Duration.ofMillis(350))
                            .ignoring(NoSuchElementException.class);
            } else {
                localAndroid=false;
                System.out.println("!!!!!!!!!!!!!!!!!!!!!!!!!!!İos Test baslıyor!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
                // capabilities.setCapability(MobileCapabilityType.NO_RESET, false);
                    DesiredCapabilities overridden = new DesiredCapabilities();;
//                    overridden.setCapability("noReset", false);
                    overridden.setCapability(MobileCapabilityType.FULL_RESET, false);
//                    overridden.setCapability("usePrebuiltWDA", true); //changed
                    overridden.setCapability("key", System.getenv("key"));
                    overridden.setCapability("appium:bundleId", "com.gratis.ios");
//                    overridden.setCapability("appium:usePrebuiltWDA",true);
//                    overridden.setCapability("appium:useNewWDA", false);
//                    overridden.setCapability("appium:autoAcceptAlerts",false);
                    driver = new TestiniumIOSDriver(hubUrl, overridden);


                    driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);
                    appiumFluentWait = new FluentWait<AppiumDriver>(driver);
                    appiumFluentWait.withTimeout(Duration.ofSeconds(8))
                            .pollingEvery(Duration.ofMillis(350))
                            .ignoring(NoSuchElementException.class);
            }
        }
//        selector = SelectorFactory
//                .createElementHelper(localAndroid ? SelectorType.ANDROID : SelectorType.IOS);
        selector = SelectorFactory.createElementHelper(
                (localAndroid || TestiniumEnvironment.isPlatformAndroid())
                        ? SelectorType.ANDROID
                        : SelectorType.IOS
        );

        driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);
        appiumFluentWait = new FluentWait<AppiumDriver>(driver);
        appiumFluentWait.withTimeout(Duration.ofSeconds(8))
                .pollingEvery(Duration.ofMillis(350))
                .ignoring(NoSuchElementException.class);



    }

    @AfterScenario
    public void afterScenario() {
        if(driver != null)
            driver.quit();
    }

}
