package com.testinium;

import com.google.appengine.repackaged.com.google.common.collect.ImmutableMap;
import com.testinium.helper.RandomString;
import com.testinium.helper.StoreHelper;
import com.testinium.model.SelectorInfo;
import com.thoughtworks.gauge.Step;
import io.appium.java_client.MobileBy;
import io.appium.java_client.TouchAction;
import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.android.nativekey.AndroidKey;
import io.appium.java_client.android.nativekey.KeyEvent;
import io.appium.java_client.ios.IOSDriver;
import io.appium.java_client.remote.HideKeyboardStrategy;
import io.appium.java_client.touch.WaitOptions;
import io.appium.java_client.touch.offset.PointOption;
import org.apache.commons.io.FileUtils;
import org.assertj.core.api.Assert;
import org.assertj.core.api.Assertions;
import org.openqa.selenium.*;
import org.openqa.selenium.interactions.*;
import org.openqa.selenium.interactions.Sequence;
import org.openqa.selenium.interactions.PointerInput;

import java.time.Duration;
import org.openqa.selenium.support.ui.ExpectedCondition;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.apache.poi.ss.usermodel.*;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import java.io.*;
import java.sql.SQLOutput;
import java.text.DecimalFormat;
import java.util.NoSuchElementException;
import java.util.Random;
import javax.annotation.Nullable;
import javax.imageio.ImageIO;
import java.sql.Timestamp;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.Duration;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.*;
import java.util.concurrent.TimeUnit;

import static java.time.Duration.ofMillis;
import static org.junit.jupiter.api.Assertions.*;

import io.appium.java_client.MobileBy;
import org.openqa.selenium.Keys;

public class StepImpl extends HookImpl {
    private static final PointerInput FINGER = new PointerInput(PointerInput.Kind.TOUCH, "finger");

    private Logger logger = LoggerFactory.getLogger(getClass());
    public StepImpl() {

    }


























    public boolean doesElementExistByKey(String key, int timeInSeconds) {
        SelectorInfo selectorInfo = selector.getSelectorInfo(key);
        try {
            WebDriverWait elementExist = new WebDriverWait(HookImpl.driver, Duration.ofSeconds(timeInSeconds));
            elementExist.until(ExpectedConditions.visibilityOfElementLocated(selectorInfo.getBy()));
            return true;
        } catch (Exception e) {
            logger.info(key + " aranan elementi bulamadı");
            return false;
        }
    }





    public WebElement findElement(By by) throws Exception {
        WebElement WebElement;
        try {
            WebElement = findElements(by).get(0);
        } catch (Exception e) {
            throw e;
        }
        return WebElement;
    }



    public List<WebElement> findElements(By by) throws Exception {
        List<WebElement> webElementList = null;
        try {
            webElementList = appiumFluentWait.until(new ExpectedCondition<List<WebElement>>() {
                @Nullable
                @Override
                public List<WebElement> apply(@Nullable WebDriver driver) {
                    List<WebElement> elements = driver.findElements(by);
                    return elements.size() > 0 ? elements : null;
                }
            });

            if (webElementList == null) {
                throw new NullPointerException(String.format("by = %s Web element list not found", by.toString()));
            }

        } catch (Exception e) {
            throw e;
        }
        return webElementList;
    }

    public WebElement findElementByKey(String key) {
        SelectorInfo selectorInfo = selector.getSelectorInfo(key);

        WebElement mobileElement = null;
        try {
            mobileElement = selectorInfo.getIndex() > 0 ? findElements(selectorInfo.getBy())
                    .get(selectorInfo.getIndex()) : findElement(selectorInfo.getBy());
        } catch (Exception e) {
            Assertions.fail("key = %s by = %s Element not found ", key, selectorInfo.getBy().toString());
            e.printStackTrace();
        }
        return mobileElement;
    }



    public WebElement findElementByKeyWithoutAssert(String key) {
        SelectorInfo selectorInfo = selector.getSelectorInfo(key);
        if (selectorInfo == null) {
            logger.warn("SelectorInfo bulunamadı! Key: " + key);
            return null;
        }

        try {
            if (selectorInfo.getIndex() > 0) {
                return findElements(selectorInfo.getBy()).get(selectorInfo.getIndex());
            } else {
                return findElement(selectorInfo.getBy());
            }
        } catch (Exception e) {
            logger.error("Element bulunamadı. Key: " + key + " Hata: " + e.getMessage());
            return null;
        }
    }




    @Step({"<seconds> saniye bekle", "Wait <second> seconds"})
    public void waitBySecond(int seconds) {
        try {
            TimeUnit.SECONDS.sleep(seconds);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    @Step("<key> li element varsa tıkla")
    public void tapElementWithKeyControl(String key) {

        logger.info("element varsa verilen tıkla ya girdi");
        WebElement mobileElement;

        mobileElement = findElementByKeyWithoutAssert(key);

        if (mobileElement != null) {

            doesElementExistByKey(key, 2);
            findElementByKey(key).click();
            logger.info(key + "elemente tıkladı");

        }
    }

    @Step("Konum izni popup'ında varsa <text> butonuna tıkla")
    public void konumIzniAlertVarsaTikla(String text) {
        try {
            HashMap<String, String> args = new HashMap<>();
            args.put("action", "accept");
            args.put("buttonLabel", text);

            ((JavascriptExecutor) driver).executeScript("mobile: alert", args);
            System.out.println("mobile: alert ile '" + text + "' butonuna tıklandı.");
        } catch (Exception e) {
            System.out.println("Alert bulunamadı veya '" + text + "' butonu tıklanamadı. Devam ediliyor...");

        }
    }

    @Step({"Check if element <key> exists",
            "Wait for element to load with key <key>",
            "Element var mı kontrol et <key>",
            "Elementin yüklenmesini bekle <key>"})
    public WebElement getElementWithKeyIfExists(String key) throws InterruptedException {
        WebElement element;
        //   SelectorInfo selectorInfo = selector.getSelectorInfo(key);
        try {
            element = findElementByKey(key);
            logger.info(key + " elementi bulundu.");
        } catch (Exception ex) {
            logger.info("Element: '" + key + "' doesn't exist.");
            // Assertions.fail("key = %s by = %s Element not found ", key,selectorInfo.getBy().toString());
            return null;
        }
        return element;
    }

    @Step({"Elementi var mı kontrol et <key>"})
    public WebElement getElementWithKeyIfExistss(String key) {
        WebElement element = null;
        try {
            By by = selector.getSelectorInfo(key).getBy(); // senin framework'e özel olabilir
            WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
            element = (WebElement) wait.until(ExpectedConditions.presenceOfElementLocated(by));
            logger.info("Element bulundu: " + key);
        } catch (TimeoutException te) {
            logger.warn("Timeout! Element görünmedi: " + key);
        } catch (NoSuchElementException ne) {
            logger.warn("Element bulunamadı: " + key);
        } catch (Exception e) {
            logger.error("Element hatası: " + key + " → " + e.getMessage());
        }
        return element;
    }

}
























